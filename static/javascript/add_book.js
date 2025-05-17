function add_book() {
    if (document.getElementById("bookId").value.length == 0) {
        alert("book id is empty!");
        return true;
    }

    if (document.getElementById("bookName").value.length == 0) {
        alert("book name is empty!");
        return true;
    }

    else {
        alert("book is added succesfully");
    }
}
