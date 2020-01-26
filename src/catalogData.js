export const catalogData = {
    shirts: [
        {
            src: 'https://lp2.hm.com/hmgoepprod?set=source[/c8/78/c8785457e25bbd6f8976c8242981e266ff387e42.jpg],origin[dam],category[men_shirts_casual],type[DESCRIPTIVESTILLLIFE],res[m],hmver[2]&call=url[file:/product/main]',
            name: 'Linen Shirt',
            brand: 'H&M'
        },
        {
            src: 'https://eultsimages.blob.core.windows.net/product-variant-images/22756272_SearchResults.jpg',
            name: 'White Pin Dot Shirt',
            brand: 'Lacoste'
        },
        {
            src: 'https://tommy-europe.scene7.com/is/image/TommyEurope/TT0TT06855_0YD_main?$main@2x$',
            name: 'Rower Point Collar Slim Fit Shirt',
            brand: 'Tommy Hilfiger'
        },
        {
            src: 'https://oldnavy.gap.com/webcontent/0017/927/929/cn17927929.jpg',
            name: 'Slim-Fit Built-In Flex Signature Non-Iron Shirt for Men',
            brand: 'Old Navy'
        },
        {
            src: 'https://anf.scene7.com/is/image/anf/KIC_125-9156-0996-201_prod1?$product-anf-v1$&wid=800&hei=1000',
            name: 'Signature Fit Oxford Shirt',
            brand: 'Abercrombie & Fitch'
        },
        {
            src: 'https://cdn.shopify.com/s/files/1/0017/2100/8243/products/SFX-1_FRONT_DOLPHIN_2000x.jpg?v=1555356949',
            name: 'Logan Snap Front Shirt - SFX-1',
            brand: 'Stormtech'
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
        },
        {
            src: 'https://imagena1.lacoste.com/dw/image/v2/AAUP_PRD/on/demandware.static/-/Sites-master/default/dw766f01fc/HH9553_PQ8_24.jpg?imwidth=767&impolicy=product',
            name: 'Slim Fit Stretch Gabardine Chino Pants',
            brand: 'Lacoste'
        },
        {
            src: 'https://imagena1.lacoste.com/dw/image/v2/AAUP_PRD/on/demandware.static/-/Sites-master/default/dw00e2fe5d/HH5541_02S_24.jpg?imwidth=767&impolicy=product',
            name: 'Motion Ergonomic Pants',
            brand: 'Lacoste'
        },
        {
            src: 'https://www.rlmedia.io/is/image/PoloGSI/s7-1350026_lifestyle?$rl_df_pdp_5_7_lif$',
            name: 'Stretch Slim Fit Chino Pant',
            brand: 'Lacoste'
        },
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