$(document).ready(function () {
    $(`.delete-product`).on('click', function () {
        let productId = $(this).data('pk')
        let product = $(this).data("name")
        $(".modal-title").html(`Delete ${product} ?`)
        $('#delete_confirm_popup').modal('show');
        $('#delete_agency').attr("href", "/product/delete/" + productId)
    })
    $(`.delete-category`).on('click', function () {
        let categoryId = $(this).data('pk')
        let category = $(this).data("name")
        $(".modal-title").html(`Delete ${category} ?`)
        $('#delete_confirm_popup').modal('show');
        $('#delete_agency').attr("href", "/category/delete/" + categoryId)
    })
    $(`.delete-cart-product`).on('click', function () {
        let cartId = $(this).data('pk')
        let name = $(this).data('name')
        $(".modal-title").html(`Remove ${name} from cart ?`)
        $('#deleteCartProduct').modal('show');
        $('#removeProduct').attr("href", "/cart/delete/" + cartId)
    })
});