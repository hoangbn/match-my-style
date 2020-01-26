from flask import Flask, request, jsonify
from google.cloud import vision

prodSet_to_prods = {}
LOCATION = 'us-east1'
PROJECT_ID =  'matchmystyle'

app = Flask(__name__)

# user_data = {
#                 "shirts": [], 
#                 "pants": []
#             }
# cata_data = {
#                 "shirts": [], 
#                 "pants": []
#             }

def create_product_set(project_id, location, product_set_id, product_set_display_name):
    """Create a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_set_display_name: Display name of the product set.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(
        project=project_id, location=location)

    # Create a product set with the product set specification in the region.
    product_set = vision.types.ProductSet(
            display_name=product_set_display_name)

    # The response is the product set with `name` populated.
    response = client.create_product_set(
        parent=location_path,
        product_set=product_set,
        product_set_id=product_set_id)
    prodSet_to_prods[product_set_id] = []

    # Display the product set information.
    print('Product set name: {}'.format(response.name))


def create_product(project_id, location, product_id, product_display_name, product_category):
    """Create one product.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_display_name: Display name of the product.
        product_category: Category of the product.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(project=project_id, location=location)

    # Create a product with the product specification in the region.
    # Set product display name and product category.
    product = vision.types.Product(
        display_name=product_display_name,
        product_category=product_category)

    # The response is the product with the `name` field populated.
    response = client.create_product(
        parent=location_path,
        product=product,
        product_id=product_id)

    # Display the product information.
    print('Product name: {}'.format(response.name))


def add_product_to_product_set(project_id, location, product_id, product_set_id):
    """Add a product to a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_set_id: Id of the product set.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product set.
    product_set_path = client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Add the product to the product set.
    client.add_product_to_product_set(
        name=product_set_path, product=product_path)
    prodSet_to_prods[product_set_id].append(product_id)

    print('Product added to product set.')


def create_reference_image(project_id, location, product_id, reference_image_id, gcs_uri):
    """Create a reference image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        reference_image_id: Id of the reference image.
        gcs_uri: Google Cloud Storage path of the input image.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Create a reference image.
    reference_image = vision.types.ReferenceImage(uri=gcs_uri)

    # The response is the reference image with `name` populated.
    image = client.create_reference_image(
        parent=product_path,
        reference_image=reference_image,
        reference_image_id=reference_image_id)

    # Display the reference image information.
    print('Reference image name: {}'.format(image.name))
    print('Reference image uri: {}'.format(image.uri))


def get_similar_products_uri(project_id, location, product_set_id, product_category, image_uri, filter):
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        file_path: Local file path of the image to be searched.
        filter: Condition to be applied on the labels.
        Example for filter: (color = red OR color = blue) AND style = kids
        It will search on all products with the following labels:
        color:red AND style:kids
        color:blue AND style:kids
    """
    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    # Create annotate image request along with product search feature.
    image_source = vision.types.ImageSource(image_uri=image_uri)
    image = vision.types.Image(source=image_source)

    # product search specific parameters
    product_set_path = product_search_client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)
    product_search_params = vision.types.ProductSearchParams(
        product_set=product_set_path,
        product_categories=[product_category],
        filter=filter)
    image_context = vision.types.ImageContext(
        product_search_params=product_search_params)

    # Search products similar to the image.
    response = image_annotator_client.product_search(
        image, image_context=image_context)

    index_time = response.product_search_results.index_time
    print('Product set index time:')
    print('  seconds: {}'.format(index_time.seconds))
    print('  nanos: {}\n'.format(index_time.nanos))

    results = response.product_search_results.results

    print('Search results:')
    for result in results:
        product = result.product

        print('Score(Confidence): {}'.format(result.score))
        print('Image name: {}'.format(result.image))

        print('Product name: {}'.format(product.name))
        print('Product display name: {}'.format(
            product.display_name))
        print('Product description: {}\n'.format(product.description))
        print('Product labels: {}\n'.format(product.product_labels))


def cleanProductIds(project_id, location, product_id):
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Delete a product.
    client.delete_product(name=product_path)
    print('Product deleted.')

def cleanProductSets(project_id, location, product_set_id):
    client = vision.ProductSearchClient()

    # Get the full path of the product set.
    product_set_path = client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)

    # Delete the product set.
    client.delete_product_set(name=product_set_path)
    print('Product set deleted.')

def cleanAll(project_id, location):

    # clean all prod_ids
    for list in prodSet_to_prods.values():
        for prod_ids in list:
            cleanProductIds(project_id, location, prod_ids)
    
    # clean prod sets
    for prod_sets in prodSet_to_prods:
        cleanProductSets(project_id, location, prod_sets)
    

@app.route("/getSimilar")
def get_most_similar():
    threshold = request.args.get("percentage")
    item = request.args.get("item")

    create_product_set(PROJECT_ID, LOCATION, '1212', 'shirts')
    create_product_set(PROJECT_ID, LOCATION, '1213', 'pants')
    create_product(PROJECT_ID, LOCATION, 'del', 'shirt1', 'apparel-v2')
    create_product(PROJECT_ID, LOCATION, 'del2', 'shirt1', 'apparel-v2')
    add_product_to_product_set(PROJECT_ID, LOCATION, 'del', '1212')
    add_product_to_product_set(PROJECT_ID, LOCATION, 'del2', '1213')
    cleanAll(PROJECT_ID, LOCATION)
    prodSet_to_prods = {}
    return 'hello there'




if __name__ == '__main__':
    app.run()