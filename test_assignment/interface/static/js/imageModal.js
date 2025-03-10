$(document).ready(function () {
    //Edit modal popup.

    $(`.fa-pencil`).on('click', function () {
        let productImageId = $(this).data('pk')
        if ($("#productImagesForm")[0]) {
            $("#productImagesForm")[0].reset()
        }
        $("#image-error-text").html("")
        $('#editImages').attr("data-pk", productImageId)
        $(".modal-title").html(`Edit Image`)
        $('#editConfirmModal').modal('show')
    })
    $(`.fa-trash`).on('click', function () {
        let productImageId = $(this).data('pk')
        $('#deleteConfirmModal').modal('show')
        $('#deleteImage').attr("href", "/product/image/delete/" + productImageId)
        $(".modal-title").html(`Delete this Image?`)
    })
})