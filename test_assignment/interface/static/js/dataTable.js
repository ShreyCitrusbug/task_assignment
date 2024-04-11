$(document).ready(function () {
    $("#productTable").DataTable({
        paging: true,
        responsive: true,
        pageLength: 5,
        autoWidth: false,
        lengthMenu: [2, 5, 10, 20, 50],
        searching: true,
        processing: true,
        columns: [
            { data: "name", name: "name" },
            { data: "price", name: "price" },
            { data: "sell_price", name: "sell_price" },
            { data: "category", name: "category" },
            { data: "created_at", name: "created_at" },
            { data: "actions", name: "actions" },
        ],
        columnDefs: [{ orderable: true, targets: [5] }],
    })
    $("#categoryTable").DataTable({
        paging: true,
        responsive: true,
        pageLength: 5,
        autoWidth: false,
        lengthMenu: [2, 5, 10, 20, 50],
        searching: true,
        processing: true,
        columns: [
            { data: "name", name: "name" },
            { data: "created_at", name: "created_at" },
            { data: "actions", name: "actions" },
        ],
        columnDefs: [{ orderable: true, targets: [2] }],
    })
    $("#cartTable").DataTable({
        paging: true,
        responsive: true,
        pageLength: 5,
        autoWidth: false,
        lengthMenu: [2, 5, 10, 20, 50],
        searching: true,
        processing: true,
        columns: [
            { data: "name", name: "name" },
            { data: "price", name: "price" },
            { data: "image", name: "product_image" },
            { data: "category", name: "category" },
            { data: "created_at", name: "created_at" },
            { data: "quantity", name: "quantity" },
            { data: "actions", name: "actions" },
        ],
        columnDefs: [{ orderable: true, targets: [2] }],
    })
})