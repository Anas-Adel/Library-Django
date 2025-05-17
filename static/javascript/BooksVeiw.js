

document.addEventListener('DOMContentLoaded', function() {

const booksForm = document.getElementById("adminForm");
const bookCont = document.querySelector(".books");
const bookTitle = booksForm['t']
const bookAuthor = booksForm['a']
const bookID = booksForm['i']
const booksCatagori= booksForm['g']
const cPersonal = document.querySelector(".personalGrowth")
const cFinanc = document.querySelector(".financ")
const cRomance = document.querySelector(".Romance")
const cKids = document.querySelector(".Kids")
const catagoryHead = booksForm['catagory']
const bigCont = document.querySelector(".booksCont")



/*function creatCatagory(catagory){
    const cHeader = document.createElement('h2')
    cHeader.innerText = catagory
    bookCont.insertAdjacentElement('afterend', cHeader)
}


let booksCatagories= JSON.parse(localStorage.getItem("booksCatagories")) || [];


function addCatg(catagory){
    booksCatagories.push(catagory)
    localStorage.setItem("booksCatagories",JSON.stringify(booksCatagories));
    return catagory
}

booksCatagories.forEach(creatCatagory);

catagoryButton.addEventListener('click', function(event2){
    event2.preventDefault();
    const newCatg = addCatg(catagoryHead.value);
    creatCatagory(newCatg);
});
*/


////////////////////////////////////////////////////////////////////

let liabarayBooks= JSON.parse(localStorage.getItem("liabarayBooks")) || [];

 function creatBook({t,a,i,c}){
    const Cont = document.createElement('div')
    const Title = document.createElement('h3')
    const Author = document.createElement('p')
    const ID = document.createElement('p')
    const Catagory = document.createElement('p')

    Title.innerText = "Title: " + t
    Author.innerText =  "Author: " + a
    ID.innerText = "ID:" + '-' +i+ '-'
    Catagory.innerText = "Catagory: " + c

    
    Cont.append(Title, Author, ID,Catagory)
  
    
    if (c === "financ") {
        cFinanc.append(Cont.cloneNode(true));
    } 
    else if(c === "personal growth" ) {
        cPersonal.append(Cont.cloneNode(true));
    }
    else if(c === "romance" ) {
        cRomance.append(Cont.cloneNode(true));
    }
    else if(c === "kids" ) {
        cKids.append(Cont.cloneNode(true));
    }
 
 }
    
    
   





    
function addBook(t, a,i, c){
     liabarayBooks.push({
        t:t,
        a:a,
        i:i, 
        c:c
    })

    localStorage.setItem("liabarayBooks",JSON.stringify(liabarayBooks));

     return {t, a, i, c}
}


liabarayBooks.forEach(creatBook);


booksForm.addEventListener('submit', function(event){
    event.preventDefault();

    const newBook = addBook(
       bookTitle.value,
       bookAuthor.value, 
       bookID.value,
       booksCatagori.value
    );
    creatBook(newBook);
 });

});


function search() {
    alert("There is no books yet.");
}