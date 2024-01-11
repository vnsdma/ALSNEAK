<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - Products</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1 class="mb-4">Dashboard - Products</h1>

        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createProductModal">
            Add Product
        </button>
        {% block y %}
            {% if session.username %}
                You are Register {{ session.username }} <a href="/logout">logout</a>.
            {% else %}
                You are not Register. <a href="/login">login</a>.
            {% endif %}
        {% endblock %}

        <!-- Modal for creating a product -->
        <div class="modal fade" id="createProductModal" tabindex="-1" aria-labelledby="createProductModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="createProductModalLabel">Create Product</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <!-- Create Product Form -->
                        <form id="createProductForm">
                            <div class="mb-3">
                                <label for="productName" class="form-label">Product Name</label>
                                <input type="text" class="form-control" id="name" placeholder="Enter product name" required>
                            </div>
                            <!-- Rest of the form fields -->
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody id="productTableBody">
                <!-- Loop through products and generate table rows -->
                <!-- BEGIN: productLoop -->
                <?php
                // Connect to the database
                $conn = mysqli_connect("localhost", "username", "password", "database_name");

                // Check connection
                if (!$conn) {
                    die("Connection failed: " . mysqli_connect_error());
                }

                // Perform the select query
                $sql = "SELECT * FROM products";
                $result = mysqli_query($conn, $sql);

                // Loop through the query results and generate table rows
                if (mysqli_num_rows($result) > 0) {
                    while ($row = mysqli_fetch_assoc($result)) {
                        echo "<tr>";
                        echo "<td>" . $row['id'] . "</td>";
                        echo "<td>" . $row['name'] . "</td>";
                        echo "<td>" . $row['price'] . "</td>";
                        echo "<td>";
                        echo "<button class='btn btn-sm btn-warning' onclick='editProductModal(" . $row['id'] . ")' data-bs-toggle='modal' data-bs-target='#editProductModal'>Edit</button>";
                        echo "<button class='btn btn-sm btn-danger' onclick='deleteProduct(" . $row['id'] . ")'>Delete</button>";
                        echo "</td>";
                        echo "</tr>";
                    }
                } else {
                    echo "<tr><td colspan='4'>No products found</td></tr>";
                }

                // Close the database connection
                mysqli_close($conn);
                ?>
                <!-- END: productLoop -->
            </tbody>
        </table>
    </div>
</body>
</html>
                                            <tbody id="productTableBody">
                                                <!-- Loop through products and generate table rows -->
                                                <!-- BEGIN: productLoop -->
                                                <tr>
                                                    <td><!-- product.id --></td>
                                                    <td><!-- product.name --></td>
                                                    <td><!-- product.price --></td>
                                                    <td>
                                                        <button class="btn btn-sm btn-warning" onclick="editProductModal(<!-- product.id -->)" data-bs-toggle="modal" data-bs-target="#editProductModal">Edit</button>
                                                        <button class="btn btn-sm btn-danger" onclick="deleteProduct[id]">Delete</button>
                                                    </td>
                                                </tr>
                                                <!-- END: productLoop -->
                                            </tbody>
                                        </table>
