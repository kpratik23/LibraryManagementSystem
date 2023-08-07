
{
    document.querySelectorAll(".leftlist").forEach(element=>{
        element.addEventListener("click",colorText)
    })

    document.querySelectorAll(".leftlist").forEach(element=>{
        element.addEventListener("click",setMarker)
    })

    document.querySelector(".issuebook").addEventListener("click",issuebook);

    document.querySelector(".submitbook").addEventListener("click",submitbook);

    document.querySelector(".submitedbook").addEventListener("click",submitedbook);

    document.querySelector(".icon").addEventListener("click",info);

    document.querySelector(".issuesubmit").addEventListener("click",issuesubmit);

    // document.querySelectorAll(".right-half button").forEach(element=>{
    //     element.addEventListener("click",hideInfo);
    // })


    document.querySelector(".issuedbook").addEventListener("click",issuedbook);

    document.querySelector(".showbooks").addEventListener("click",showbooks);

    document.querySelector(".addbtn").addEventListener("click",booksubmit);

    document.querySelector(".addbook").addEventListener("click",addbook);

    document.querySelector(".edit").addEventListener("click",editInfo);

    document.querySelector(".delete").addEventListener("click",deleteInfo);

    document.querySelector(".submitinfo").addEventListener("click",submitinfo);

    setInitialMarker();

    currentID=null;
}

function resetTabs(){
    document.querySelector(".issue").style.display="none";
    document.querySelector(".submit").style.display="none";
    document.querySelector(".issued").style.display="none";
    document.querySelector(".submited").style.display="none";
    document.querySelector(".books").style.display="none";
    document.querySelector(".newbooks").style.display="none";
}

function setInitialMarker(){
    firstTabtop=document.querySelector(".active").offsetTop;
    firstTabHeight=document.querySelector(".active").offsetHeight;
    document.querySelector(".marker").style.top=firstTabtop+"px";
    document.querySelector(".marker").style.height=firstTabHeight+"px";

}

function colorText(event){

    document.querySelector(".active").classList.remove("active");
    event.currentTarget.classList.add("active");

}

function setMarker(event){


    markertop=event.currentTarget.offsetTop
    markerheight=event.currentTarget.offsetHeight
    marker=document.querySelector(".marker")
    marker.style.top=markertop+"px";
    marker.style.height=markerheight+"px";
}

function issuebook(){

    resetTabs();

    document.querySelector(".issue").style.display="flex"
}

function submitbook(){

    resetTabs();

    document.querySelector(".submit").style.display="flex"
}

function submitedbook(){

    // alert("Hello World !")

    resetTabs();

    $.get("http://127.0.0.1:8000/api/submit/",function(data,status){

        submitedtable=document.querySelector(".submited table")

        submitedtable.innerHTML=""

        header=`
                <th>Student id</th>
                <th>Rollno</th>
                <th>Name</th>
                <th>Bookname</th>
                <th>Branch</th>
                <th>Issued</th>
                <th>Submitted</th>
                <th>Fine</th>
                `
        submitedtable.innerHTML+=header;

        data.forEach(element=>{
            node=`<tr>
                <td>${element.studentid}</td>
                <td>${element.rollno}</td>
                <td>${element.name}</td>
                <td>${element.isbn}</td>
                <td>${element.branch}</td>
                <td>${element.issued.split("T")[0]}</td>
                <td>${element.submitdate.split("T")[0]}</td>
                <td>${element.fine}</td>
                </tr>`

                console.log(node)
                submitedtable.innerHTML+=node
        })

    })

    document.querySelector(".submited").style.display="block";
}

function info(){

    value=document.querySelector(".searchbox").value;

    if (value!=""){
        
        currentID=value;

        $.get(`http:/\/127.0.0.1:8000/api/getDetails/${value}`,function(data,status){

        console.log(status)
            
            textvalues=document.querySelectorAll(".info input");
            
            console.log(data)
            
            console.log(status)

            if (status=="success"){

                
                console.log(moment(data[0].issued).format("YYYY-MM-DDTkk:mm"))

                document.querySelector(".info").style.display="flex";

                console.log(data[0].issued)

                textvalues[0].value=data[0].name;
                textvalues[1].value=data[0].isbn;
                textvalues[2].value=data[0].branch;
                textvalues[3].value=data[0].rollno;
                textvalues[4].value=moment(data[0].issued).format("YYYY-MM-DDTkk:mm");
                textvalues[5].value=moment(data[0].submitdate).format("YYYY-MM-DDTkk:mm");

            }

            else{
                alert("Recored not found !")
            }
        })
        
        console.log(value);
    }

}

function issuesubmit(){

    
    issues=document.querySelectorAll(".issue input")

    console.log(issues)

    console.log("Hello World !")

    node=`{
        "name":"${issues[0].value}",
        "isbn":"${issues[1].value}",
        "branch":"${issues[2].value}",
        "rollno":"${issues[3].value}",
        "issued":"${issues[4].value}",
        "submitdate":"${issues[5].value}"
    }`

    console.log(node)

    $.post("http://127.0.0.1:8000/api/issuebook/",node,function(data,status){

        if(status=="success"){
            alert("Book Issued Successfully !")
        }

    })

    document.querySelectorAll(".issue input").forEach(element=>{
        element.value="";
    })
}

function hideInfo(){

    document.querySelectorAll(".left-half input").forEach(element=>{
        element.value="";
    })

    document.querySelector(".searchbox").value="";

    document.querySelector(".info").style.display="none";
    
}

function issuedbook(){
    
    resetTabs();

    document.querySelector(".issued table").innerHTML=""
    $.get("http://127.0.0.1:8000/api/issuebook",function(data,status){
        

    //     node=`
    //         <tr>
    //             <td>${}</td>
    //             <td>${} </td>
    //             <td>${}</td>
    //             <td>${}</td>
    //             <td>${}</td>
    //         </tr>
    // `
    
    // alert("Successful GET request !");
    

        node=`<th>Student Id</th>
        <th>Rollno</th>
        <th>Name</th>
        <th>Book Id</th>
        <th>Branch</th>
        <th>Issued</th>
        <th>End Date</th>
        `
        document.querySelector(".issued table").innerHTML+=node;

        console.log(data)

        data.forEach(element=>{

            console.log(element.author)
            console.log(element.issued);
            console.log(element.submitdate);
            node=
            `
            <tr>
                <td>${element.studentid}</td>
                <td>${element.rollno}</td>
                <td>${element.name} </td>
                <td>${element.isbn}</td>
                <td>${element.branch}</td>
                <td>${element.issued.split("T")[0]}</td>
                <td>${element.submitdate.split("T")[0]}</td>
            </tr>`

            console.log(node)

            document.querySelector(".issued table").innerHTML+=node;
        })

    })

    document.querySelector(".issued").style.display="block";
}

function showbooks(){
    
    resetTabs();
    
    document.querySelector(".books table").innerHTML=""
    $.get("http://127.0.0.1:8000/api/listbooks ",function(data,status){
        

    //     node=`
    //         <tr>
    //             <td>${}</td>
    //             <td>${} </td>
    //             <td>${}</td>
    //             <td>${}</td>
    //             <td>${}</td>
    //         </tr>
    // `
    
    // alert("Successful GET request !");
    

        node=`<th>ISBN</th>
            <th>Book Name</th>
            <th>Author</th>
            <th>Publication</th>
            <th>Quantity</th>
        `
        document.querySelector(".books table").innerHTML+=node;


        data.forEach(element=>{

            console.log(element.author)
            node=
            `
            <tr>
                <td>${element.isbn}</td>
                <td>${element.bookname} </td>
                <td>${element.author}</td>
                <td>${element.publication}</td>
                <td>${element.quantity}</td>
            </tr>`
            document.querySelector(".books tbody").innerHTML+=node;
        })

    })

    document.querySelector(".books").style.display="block";
}

function booksubmit(){
    
    newbooks=document.querySelectorAll(".newbooks input")

    console.log(newbooks)

    console.log("Hello World !")

    node=`{
        "isbn":${newbooks[0].value},
        "bookname":"${newbooks[1].value}",
        "author":"${newbooks[2].value}",
        "publication":"${newbooks[3].value}",
        "quantity":${newbooks[4].value}
    }`

    console.log(node)

    $.post("http://127.0.0.1:8000/api/addbook/",node,function(data,status){

        console.log(data)

    })

    document.querySelectorAll(".newbooks input").forEach(element=>{
        element.value="";
    })
}

function addbook(){
    
    resetTabs();



    document.querySelector(".newbooks").style.display="flex";
}

function editInfo(){


    node=document.querySelectorAll(".left-half input")

    console.log(currentID)

    
    
    
    data=`{   
        "studentid":${currentID},
        "name":"${node[0].value}",
        "isbn":"${node[1].value}",
        "branch":"${node[2].value}",
        "rollno":"${node[3].value}",
        "issued":"${node[4].value}",
        "submitdate":"${node[5].value}"
    }`
    
    console.log(data)
    
    $.ajax({
        url: 'http://127.0.0.1:8000/api/edit/',
        type: 'PUT',
        data: data,
        success: function(result) {
            alert("Updated successfully !")
        },
        error: function(){
            alert("An error occuerd !")
        }
    });

    hideInfo();
}


function deleteInfo(){
    
    $.ajax({
        url: 'http://127.0.0.1:8000/api/delete/',
        type: 'DELETE',
        data: data,
        success: function(result) {
            alert("Deleted successfully !")
        },
        error: function(){
            alert("An error occuerd !")
        }
    });

    hideInfo();

}

function submitinfo(){

    inputtext=document.querySelectorAll(".left-half input");

    node=`{   
        "studentid":${currentID},
        "name":"${inputtext[0].value}",
        "isbn":"${inputtext[1].value}",
        "branch":"${inputtext[2].value}",
        "rollno":"${inputtext[3].value}",
        "issued":"${inputtext[4].value}",
        "submitdate":"${inputtext[5].value}"
    }`

    console.log(node)

    $.post("http://127.0.0.1:8000/api/submit/",node,function(data,status){

        if (status=="success"){
            alert("Book submitted successfully !")
        }

    })

    hideInfo();

}