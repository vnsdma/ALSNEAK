<script>
        fetch('/product')
        .then(response => response.json())
        .then(data => {
            const productTableBody = document.getElementById('productTableBody');
            data.forEach(product => {
            productTableBody.innerHTML += `
                    <tr>
                        <td>${product.id}</td>
                        <td>${product.name}</td>
                        <td>${product.price}</td>
                        <!-- Add other product attributes as table cells -->
                        <td>
                            <button class="btn btn-sm btn-warning" data-bs-target="#editProductModal" data-bs-toggle="modal">Edit</button>
                            <button class="btn btn-sm btn-danger" data-toggle="modal"
                                data-target="#delete_book_{{product['id']}}">Delete</button>
                        </td>
                    </tr>
                    `;
                });
            })
            .catch(error => console.error('Error:', error));

            document.getElementById('createProductForm').addEventListener('submit', function(event) {
            event.preventDefault();

            let name = document.getElementById('name').value;
            let price = document.getElementById('price').value;
            let category_id = document.getElementById('category_id').value;
            // Create an object with product data
            const productData = {
                name: name,
                price: price,
                category_id: category_id
                // Add more properties for other product attributes if needed
            };

            // Send a POST request to create the product
            fetch('/product', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(productData),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response or close the modal
                console.log('Product created:', data);
                // Close the modal after creating the product
                const createProductModal = new bootstrap.Modal(document.getElementById('createProductModal'));
                createProductModal.hide();
                // Reload the page after creating the product
                window.location.reload();
            })
            .catch(error => {
                console.error('Error:', error);
            });
            
        });
        fetch('/category') // Fetch categories from Flask backend
            .then(response => response.json())
            .then(data => {
                const categorySelect = document.getElementById('category_id');

                data.forEach(category => {
                    const option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = category.name;
                    categorySelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
            function openEditModal(productId) {
                // Set the product ID in the hidden input field of the edit form
                document.getElementById('productId').value = productId;

                // Fetch product details for the given ID and populate the form fields for editing
                fetch(`/product/${productId}`)
                    .then(response => response.json())
                    .then(product => {
                        document.getElementById('productName').value = product.name;
                        // Populate other form fields with product details for editing
                        })
                        .catch(error => console.error('Error:', error));
                    }
                    </script>
