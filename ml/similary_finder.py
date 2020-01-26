from flask import Flask, request, jsonify
from google.cloud import vision

prodSet_to_prods = {}
LOCATION = 'us-east1'
PROJECT_ID =  'matchmystyle'
CATEGORY = "apparel-v2"
GCS_LINK = ""
export const catalogData = {
    shirts: [
        {
            src: 'https://lp2.hm.com/hmgoepprod?set=source[/c8/78/c8785457e25bbd6f8976c8242981e266ff387e42.jpg],origin[dam],category[men_shirts_casual],type[DESCRIPTIVESTILLLIFE],res[m],hmver[2]&call=url[file:/product/main]',
            uri: 'gs://matchmystyle-vcm/shirts/hmgoepprod.jfif',
            name: 'Linen Shirt',
            brand: 'H&M'
        },
        {
            src: 'https://eultsimages.blob.core.windows.net/product-variant-images/22756272_SearchResults.jpg',
            uri: 'gs://matchmystyle-vcm/shirts/22756272_SearchResults.jpg',
            name: 'White Pin Dot Shirt',
            brand: 'Lacoste'
        },
        {
            src: 'https://tommy-europe.scene7.com/is/image/TommyEurope/TT0TT06855_0YD_main?$main@2x$',
            uri: 'gs://matchmystyle-vcm/shirts/TT0TT06855_0YD_main.webp',
            name: 'Rower Point Collar Slim Fit Shirt',
            brand: 'Tommy Hilfiger'
        },
        {
            src: 'https://oldnavy.gap.com/webcontent/0017/927/929/cn17927929.jpg',
            uri: 'gs://matchmystyle-vcm/shirts/cn17927929.webp',
            name: 'Slim-Fit Built-In Flex Signature Non-Iron Shirt for Men',
            brand: 'Old Navy'
        },
        {
            src: 'https://anf.scene7.com/is/image/anf/KIC_125-9156-0996-201_prod1?$product-anf-v1$&wid=800&hei=1000',
            uri: 'gs://matchmystyle-vcm/shirts/KIC_125-9156-0996-201_prod1.webp',
            name: 'Signature Fit Oxford Shirt',
            brand: 'Abercrombie & Fitch'
        },
        {
            src: 'https://cdn.shopify.com/s/files/1/0017/2100/8243/products/SFX-1_FRONT_DOLPHIN_2000x.jpg?v=1555356949',
            uri: 'gs://matchmystyle-vcm/shirts/SFX-1_FRONT_DOLPHIN_2000x.jpg',
            name: 'Logan Snap Front Shirt - SFX-1',
            brand: 'Stormtech'
        }
    ],
    pants: [
        {
            src: 'https://lp2.hm.com/hmgoepprod?set=source[/a4/d1/a4d14f0ad315aa0cda7574bc2fe028ab70c1ab2e.jpg],origin[dam],category[],type[DESCRIPTIVESTILLLIFE],hmver[1]&call=url[file:/product/main]',
            uri: 'gs://matchmystyle-vcm/pants/hmgoepprod (1).jfif',
            name: 'Skinny Fit Cotton Chinos',
            brand: 'H&M'
        },
        {
            src: 'https://imagena1.lacoste.com/dw/image/v2/AAUP_PRD/on/demandware.static/-/Sites-master/default/dw766f01fc/HH9553_PQ8_24.jpg?imwidth=767&impolicy=product',
            uri: 'gs://matchmystyle-vcm/pants/HH9553_PQ8_24.webp',
            name: 'Slim Fit Stretch Gabardine Chino Pants',
            brand: 'Lacoste'
        },
        {
            src: 'https://www.rlmedia.io/is/image/PoloGSI/s7-1350026_lifestyle?$rl_df_pdp_5_7_lif$',
            uri: 'gs://matchmystyle-vcm/pants/s7-1350026_lifestyle.jfif',
            name: 'Stretch Slim Fit Chino Pant',
            brand: 'Ralph Lauren'
        },
        {
            src: 'https://www.rlmedia.io/is/image/PoloGSI/s7-1356471_lifestyle?$rl_df_pdp_5_7_lif$',
            uri: 'gs://matchmystyle-vcm/pants/s7-1356471_lifestyle.jfif',
            name: 'Slim Fit Linen-Blend Pant',
            brand: 'Ralph Lauren'
        },
        {
            src: 'https://imagena1.lacoste.com/dw/image/v2/AAUP_PRD/on/demandware.static/-/Sites-master/default/dw00e2fe5d/HH5541_02S_24.jpg?imwidth=767&impolicy=product',
            uri: 'gs://matchmystyle-vcm/pants/HH5541_02S_24.webp',
            name: 'Motion Ergonomic Pants',
            brand: 'Lacoste'
        },
        {
            src: 'https://lp2.hm.com/hmgoepprod?set=source[/aa/30/aa30202e0074e5adfa8dc6e7f127c63c78f56857.jpg],origin[dam],category[men_trousers_trousers_skinny_all],type[DESCRIPTIVESTILLLIFE],hmver[1]&call=url[file:/product/main]',
            uri: 'gs://matchmystyle-vcm/pants/hmgoepprod.jfif',
            name: 'Twill Pants Skinny Fit',
            brand: 'H&M'
        },
    ]
}
app = Flask(__name__)

# user_data = {
#                 "shirts": [], 
#                 "pants": []
#             }
# cata_data = {
#                 "shirts": [], 
#                 "pants": []
#             }

def create_product_set(project_id, location, product_set_id1, product_set_display_name):
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
        product_set_id=product_set_id1)
    prodSet_to_prods[product_set_id1] = []

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

   
def get_similar_products_uri(project_id, location, product_set_id, product_category,image_uri, filter):
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
    print (results)
    for result in results:
        product = result.product

        print('Score(Confidence): {}'.format(result.score))
        print('Image name: {}'.format(result.image))

        print('Product name: {}'.format(product.name))
        print('Product display name: {}'.format(
            product.display_name))
        print('Product description: {}\n'.format(product.description))
        print('Product labels: {}\n'.format(product.product_labels))
iid=3

def get_similar_products_file(project_id, location, product_set_id, product_category,file_path, filter):
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

    # Read the image as a stream of bytes.
    with open(file_path, 'rb') as image_file:
        content = image_file.read()

    # Create annotate image request along with product search feature.
    image = vision.types.Image(content=content)

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
    print(results)
    for result in results:
        product = result.product

        print('Score(Confidence): {}'.format(result.score))
        print('Image name: {}'.format(result.image))

        print('Product name: {}'.format(product.name))
        print('Product display name: {}'.format(
            product.display_name))
        print('Product description: {}\n'.format(product.description))
        print('Product labels: {}\n'.format(product.product_labels))

def list_product_sets(project_id, location):
    """List all product sets.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(
        project=project_id, location=location)

    # List all the product sets available in the region.
    product_sets = client.list_product_sets(parent=location_path)

    # Display the product set information.
    for product_set in product_sets:
        print('Product set name: {}'.format(product_set.name))
        print('Product set id: {}'.format(product_set.name.split('/')[-1]))
        print('Product set display name: {}'.format(product_set.display_name))
        print('Product set index time:')
        print('  seconds: {}'.format(product_set.index_time.seconds))
        print('  nanos: {}\n'.format(product_set.index_time.nanos))

def list_products(project_id, location):
    """List all products.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(project=project_id, location=location)

    # List all the products available in the region.
    products = client.list_products(parent=location_path)

    # Display the product information.
    for product in products:
        print('Product name: {}'.format(product.name))
        print('Product id: {}'.format(product.name.split('/')[-1]))
        print('Product display name: {}'.format(product.display_name))
        print('Product description: {}'.format(product.description))
        print('Product category: {}'.format(product.product_category))
        print('Product labels: {}\n'.format(product.product_labels))

def list_reference_images(project_id, location, product_id):
    """List all images in a product.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # List all the reference images available in the product.
    reference_images = client.list_reference_images(parent=product_path)

    # Display the reference image information.
    for image in reference_images:
        print('Reference image name: {}'.format(image.name))
        print('Reference image id: {}'.format(image.name.split('/')[-1]))
        print('Reference image uri: {}'.format(image.uri))
        print('Reference image bounding polygons: {}'.format(image.bounding_polys))

def purge_products_in_product_set(project_id, location, product_set_id, force):
    """Delete all products in a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        force: Perform the purge only when force is set to True.
    """
    client = vision.ProductSearchClient()

    parent = client.location_path(
        project=project_id, location=location)

    product_set_purge_config = vision.types.ProductSetPurgeConfig(
        product_set_id=product_set_id)

    # The purge operation is async.
    operation = client.purge_products(
        parent=parent,
        product_set_purge_config=product_set_purge_config,
        # The operation is irreversible and removes multiple products.
        # The user is required to pass in force=True to actually perform the
        # purge.
        # If force is not set to True, the service raises an exception.
        force=force)

    operation.result(timeout=120)

    print('Deleted products in product set.')

@app.route("/getSimilar")
def get_most_similar():

    # threshold = request.args.get("percentage")
    # data = request.json
    # create_product_set(PROJECT_ID, LOCATION, "1", "shirts")
    # create_product_set(PROJECT_ID, LOCATION, "2", "pants")
    # for uri in range(3): # loop through shirts in user data
    #     create_product(PROJECT_ID, LOCATION, str(iid), "name", CATEGORY)
    #     create_reference_image(PROJECT_ID, LOCATION, str(iid), str(iid+1), uri)
    #     add_product_to_product_set(PROJECT_ID, LOCATION, str(iid), "1")
    #     iid+=2
    # for uri in range(3): # loop through pants in user data
    #     create_product(PROJECT_ID, LOCATION, str(iid), "name", CATEGORY)
    #     create_reference_image(PROJECT_ID, LOCATION, str(iid), str(iid+1), uri)
    #     add_product_to_product_set(PROJECT_ID, LOCATION, str(iid), "2")
    #     iid+=2    
    # for shirt in data["shirts"]:
    #     get_similar_products_uri(PROJECT_ID, LOCATION, "1", CATEGORY, shirt["src"], "")
    # for pant in data["pants"]:
    #     get_similar_products_uri(PROJECT_ID, LOCATION, "2", CATEGORY, pant["src"], "")

    #     create_product(PROJECT_ID, LOCATION, iid, shirt["name"], shirt["brand"])
    #     create_reference_image(PROJECT_ID, LOCATION, iid, )
    #     iid+=1
    # for pant in data["pants"]:
    #     create_product(PROJECT_ID, LOCATION, iid, pant["name"], pant["brand"])
    #     iid+=1
    try:
        # create_product_set(PROJECT_ID, LOCATION, 'dd', 'shirts')
        # create_product_set(PROJECT_ID, LOCATION, 'dd1', 'pants')
        # create_product(PROJECT_ID, LOCATION, 'del4', 'shirt1', CATEGORY)
        # create_product(PROJECT_ID, LOCATION, 'del5', 'pant1', CATEGORY)    
        # add_product_to_product_set(PROJECT_ID, LOCATION, 'del4', 'dd')
        # add_product_to_product_set(PROJECT_ID, LOCATION, 'del5', 'dd1')
        # create_reference_image(PROJECT_ID, LOCATION, 'del6', 'bruh1', 'gs://matchmystyle-vcm/shirts/22756272_SearchResults.jpg')
        # create_reference_image(PROJECT_ID, LOCATION, 'del6', 'bruh2', 'gs://matchmystyle-vcm/shirts/KIC_125-9156-0996-201_prod1 (1).jpg')
        # create_reference_image(PROJECT_ID, LOCATION, 'del7', 'bruh3', 'gs://matchmystyle-vcm/pants/hmgoepprod.jfif')
        # create_reference_image(PROJECT_ID, LOCATION, 'del7', 'bruh4', 'gs://matchmystyle-vcm/pants/hmgoepprod (1).jfif')
        list_product_sets(PROJECT_ID, LOCATION)
        list_products(PROJECT_ID, LOCATION)
        # purge_products_in_product_set(PROJECT_ID, LOCATION, '121212', True)
        # purge_products_in_product_set(PROJECT_ID, LOCATION, '1212123', True)

        # create_product(PROJECT_ID, LOCATION, 'shirts_cat', 'shirt1', CATEGORY)
        # add_product_to_product_set(PROJECT_ID, LOCATION, 'shirts_cat', '121212')

        # create_product(PROJECT_ID, LOCATION, 'pants_cat', 'pant1', CATEGORY)
        # add_product_to_product_set(PROJECT_ID, LOCATION, 'pants_cat', '1212123')

        # list_product_sets(PROJECT_ID, LOCATION)
        # list_products(PROJECT_ID, LOCATION)

        # get_similar_products_uri(PROJECT_ID, LOCATION, '121212', CATEGORY, 'https://tommy-europe.scene7.com/is/image/TommyEurope/TT0TT06855_0YD_main?', '')
    
    except Exception as e:
        print(e)
        # cleanAll(PROJECT_ID, LOCATION)
    cleanAll(PROJECT_ID, LOCATION)
    global prodSet_to_prods
    prodSet_to_prods = {}
    return 'hey heyyyyyyy babuu frick'




if __name__ == '__main__':
    app.run()