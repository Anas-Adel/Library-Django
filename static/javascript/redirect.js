function Add_book_redirect() {
    window.location.replace('add-book/');
    return false;
}

function book_redirect() {
    window.location.replace("../book-page/");
    return false;
}



function edit_book_redirect() {
    window.location.replace("../edit-book/");
    return false;
}

function del(book_id) {
    b_id = book_id
    window.location.replace("'../delete-book/' book_id=b_id");
    return false;
}