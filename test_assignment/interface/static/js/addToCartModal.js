$(document).ready(function () {
    $(`.add-to-cart`).on('click', function () {
        let productId = $(this).data('pk')
        let product = $(this).data("name")
        let productPrice = $(`#product-price-${productId}`).text()
        let productSellPrice = $(`#product-sell-price-${productId}`).text()
        let category = $(`#product-category-${productId}`).text()
        $(".modal-title").html(`Are you sure you want to add ${product} to cart?`)
        $('#addToCart').modal('show');
        $("#product-content").append(`<div class="row"><div class="col-4"><h6>Price</h6>${productPrice}</div><div class="col-4"><h6>Sell Price</h6>${productSellPrice}</div><div class="col-4"><h6>Category</h6>${category}</div></div>`)
        $('#addProductToCart').attr("href", "/add/cart/" + productId)
    })
});