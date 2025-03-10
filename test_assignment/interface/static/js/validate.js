$(document).ready(function () {
    // Common function for input field that accepts only numbers excludes e, +, -.
    $("input[type=number]").on("keydown", function (event) {
        var invalidChars = ["-", "+", "e", "E"];
        if (invalidChars.includes(event.key)) {
            event.preventDefault();
        }
    });
    // On wheel function to prevent wheel event for all numbers
    $("input[type=number]").on("wheel", function (event) {
        event.currentTarget.blur()
        event.preventDefault()
    })
    // Common validation for field value
    var validateField = function (value, idName, name) {
        if (value === "") {
            $(idName).html(`${name} is required.`);
            return false
        }
        else {
            $(idName).html("");
            return true
        }
    }
    //Create product validation
    $("#create-product-submit-btn").on("click", function (event) {
        let name = $("#id_name").val();
        let price = $("#id_price").val();
        let sellPrice = $("#id_sell_price").val();
        let category = $("#id_category").val();
        let description = $("#id_description").val();
        let images = $("#productImages")

        isValidPrice = true
        isValidSellPrice = true
        isFormValid = true
        if (!(validateField(name, "#name-error-text", "Product Name"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(price, "#price-error-text", "Price"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(sellPrice, "#sell-price-error-text", "Sell Price"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(category, "#category-error-text", "Category"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(description, "#description-error-text", "Description"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(images.val(), "#product-images-error-text", "Image"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (price && sellPrice && isValidPrice && isValidSellPrice) {
            if (sellPrice > price) {
                isFormValid = false
                event.preventDefault();
                $("#sell-price-error-text").html("Sell price cannot be greater than price.");
            }
        }
        if (images) {
            let isValidImageType = Array.from(images).every(image => {
                let imageType = image.files[0].name.split(".").pop().toLowerCase();
                return imageType === 'jpeg' || imageType === 'jpg' || imageType === 'png';
            });
            if (!isValidImageType) {
                isFormValid = false;
                event.preventDefault();
                $("#product-images-error-text").html("Invalid image type. Please upload images with only .jpg, .jpeg, or .png extensions.");
            }
        }
    })
    //Update product validation
    $("#update-product-submit-btn").on("click", function (event) {
        let name = $("#id_name").val();
        let price = $("#id_price").val();
        let sellPrice = $("#id_sell_price").val();
        let category = $("#id_category").val();
        let description = $("#id_description").val();
        let images = $("#images")

        isValidPrice = true
        isValidSellPrice = true
        isFormValid = true
        if (!(validateField(name, "#name-error-text", "Product Name"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(price, "#price-error-text", "Price"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(sellPrice, "#sell-price-error-text", "Sell Price"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(category, "#category-error-text", "Category"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (!(validateField(description, "#description-error-text", "Description"))) {
            isFormValid = false
            event.preventDefault();
        }
        if (price && sellPrice && isValidPrice && isValidSellPrice) {
            if (sellPrice > price) {
                isFormValid = false
                event.preventDefault();
                $("#sell-price-error-text").html("Sell price cannot be greater than price.");
            }
        }
        if (name && name.length > 250) {
            isFormValid = false
            event.preventDefault();
            $("#name-error-text").html("Name cannot be greater than 250 characters.");
        }
        if (images) {
            let isValidImageType = Array.from(images).every(image => {
                let imageType = image.files[0].name.split(".").pop().toLowerCase();
                return imageType === 'jpeg' || imageType === 'jpg' || imageType === 'png';
            });
            if (!isValidImageType) {
                isFormValid = false;
                event.preventDefault();
                $("#product-image-error-text").html("Invalid image type. Please upload images with only .jpg, .jpeg, or .png extensions.");
            }
        }
    })

    //create category form validation
    $("#create-category-submit-btn").on("click", function (event) {
        let name = $("#id_name").val();
        if (!(validateField(name, "#name-error-text", "*Category Name"))) {
            isFormValid = false
            event.preventDefault();
        }
    })

    //Validate image create form
    $("#editImages").on("click", function (event) {
        event.preventDefault()
        let isFormValid = true
        let productImage = $("#productImage").val();
        let uuid = $(this).data("pk").split("/").pop();
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

        if (!(validateField(productImage, "#image-error-text", "Image"))) {
            isFormValid = false
            event.preventDefault()
        }
        if (productImage) {
            let extension = productImage.split(".").pop().toLowerCase();
            if (
                extension !== "jpg" &&
                extension !== "jpeg" &&
                extension !== "png" &&
                extension !== "svg"
            ) {
                isFormValid = false
                event.preventDefault();
                $("#image-error-text").html(
                    "Please upload valid image type .jpg .jpeg .png or .svg."
                );
            }
        }
        if (isFormValid) {
            let formData = new FormData();
            formData.append("pk", uuid);
            formData.append("csrfmiddlewaretoken", csrfToken);
            formData.append("image", $("#productImage")[0].files[0]);
            $.ajax({
                method: "POST",
                enctype: "multipart/form-data",
                url: `/product/image/update/${uuid}`,
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    if (response.status) {
                        window.location.href = response.url
                    }
                },
                error: function (error) {
                    window.location.href = error.url
                }
            })
        }
    })
})
