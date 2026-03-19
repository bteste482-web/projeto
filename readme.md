tabelas:

    users:
        id
        username
        email
        password_hash
        created_at

    books:
        id
        title
        author
        description
        created_at

    favorites:
        id
        book_id
        user_id

    reviews
        id
        user_id
        book_id
        rating
        comment
        created_at

rotas:

    user:
        POST /register
        POST /login
        GET /profile

    Livros:
        GET /books
        GET /books/<id>
        POST /books
        PUT /books/<id>
        DELETE /books/<id>

    Favoritos:
        POST /favorites/<book_id>
        DELETE /favorites/<book_id>
        GET /favorites

    Avaliações:
        POST /reviews/<book_id>
        GET /reviews/<book_id>


ESTRUTURA: 
    library_api/

    app.py

    models/
        user.py
        book.py
        review.py
        favorite.py

    routes/
        auth_routes.py
        book_routes.py
        review_routes.py
        favorite_routes.py

    services/
        auth_service.py
        book_service.py

    database/
        db.py

    utils/
        security.py

    config.py