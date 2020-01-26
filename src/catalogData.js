export const catalogData = {
    shirts: [
        {
            src: 'https://anf.scene7.com/is/image/anf/KIC_125-9156-0996-201_prod1?$product-anf-v1$&wid=800&hei=1000',
            name: 'Signature Fit Oxford Shirt',
            brand: 'Abercrombie & Fitch'
        },
        {
            src: 'https://eultsimages.blob.core.windows.net/product-variant-images/22756272_SearchResults.jpg',
            name: 'White Pin Dot Shirt',
            brand: 'Lacoste'
        },
        {
            src: 'https://anf.scene7.com/is/image/anf/KIC_125-9156-0996-201_prod1?$product-anf-v1$&wid=800&hei=1000',
            name: 'Signature Fit Oxford Shirt',
            brand: 'Abercrombie & Fitch'
        },
        {
            src: 'https://eultsimages.blob.core.windows.net/product-variant-images/22756272_SearchResults.jpg',
            name: 'White Pin Dot Shirt',
            brand: 'Lacoste'
        },
        {
            src: 'https://anf.scene7.com/is/image/anf/KIC_125-9156-0996-201_prod1?$product-anf-v1$&wid=800&hei=1000',
            name: 'Signature Fit Oxford Shirt',
            brand: 'Abercrombie & Fitch'
        },
        {
            src: 'https://eultsimages.blob.core.windows.net/product-variant-images/22756272_SearchResults.jpg',
            name: 'White Pin Dot Shirt',
            brand: 'Lacoste'
        }
    ],
    pants: [
        {
            src: 'https://lp2.hm.com/hmgoepprod?set=source[/a4/d1/a4d14f0ad315aa0cda7574bc2fe028ab70c1ab2e.jpg],origin[dam],category[],type[DESCRIPTIVESTILLLIFE],hmver[1]&call=url[file:/product/main]',
            name: 'Skinny Fit Cotton Chinos',
            brand: 'H&M'
        },
        {
            src: 'https://lp2.hm.com/hmgoepprod?set=source[/aa/30/aa30202e0074e5adfa8dc6e7f127c63c78f56857.jpg],origin[dam],category[men_trousers_trousers_skinny_all],type[DESCRIPTIVESTILLLIFE],hmver[1]&call=url[file:/product/main]',
            name: 'Twill Pants Skinny Fit',
            brand: 'H&M'
        }
    ]
}

export const getCategoryUrls = () => {
    let output = {};
    let categoryUrl = [];
    let categories = Object.keys(catalogData);  // array of keys (i.e. shirts and pants)

    categories.forEach((categoryName) => {
        catalogData[categoryName].forEach((categoryItemData) => {
            categoryUrl.push(categoryItemData.src);
        });
        output[categoryName] = categoryUrl;
        categoryUrl = [];
    })

    return output;
}