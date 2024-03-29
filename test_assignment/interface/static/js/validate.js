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
    })
    //Update product validation
    $("#update-product-submit-btn").on("click", function (event) {
        let name = $("#id_name").val();
        let price = $("#id_price").val();
        let sellPrice = $("#id_sell_price").val();
        let category = $("#id_category").val();
        let description = $("#id_description").val();

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
    })

    //create category form validation
    $("#create-category-submit-btn").on("click", function (event) {
        let name = $("#id_name").val();
        if (!(validateField(name, "#name-error-text", "*Category Name"))) {
            isFormValid = false
            event.preventDefault();
        }
    })
})