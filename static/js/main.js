//  Main JS for Bangladesh Result website


const randomOne = Math.floor(Math.random()* (10-1)) + 1 ;
const randomTwo = Math.floor(Math.random()* (10-1)) + 1;

//  Operation of Frontend 

const show = document.getElementById('show');
show.innerHTML = `${randomOne} + ${randomTwo}`;


const result = document.getElementById('result').addEventListener("input",Runsome)
const sumbitbutton = document.getElementById('button')
sumbitbutton.disabled = true;

function Runsome(){
    const result = document.getElementById('result').value;
    const sum = randomOne + randomTwo
    if (sum == result){

        sumbitbutton.disabled  = false;
        document.getElementById('result').style.cssText = 
        "border: 1px solid green;"
    }
    else{
        // document.getElementById('button').style.display = 'none';
        sumbitbutton.disabled = true;
        document.getElementById('result').style.cssText = 
        "border : 1px solid red; "
    }

}

// $.ajax({
//     url :'',
//     type:'GET',
//     data:NamedNodeMap,
// });


document.getElementById('search').addEventListener("submit",(e) => {
    e.preventDefault();
    
    let roll = document.getElementsByName('roll')
    let regi = document.getElementsByName('regi')
    let year = document.getElementsByName('year')
    
    $.ajax({
        url : "{% url 'result' %}",
        type: "GET",
        data : {
            "roll" : roll,
            "regi" : regi,
            "year" : year
        },
        success : function(){
            console.log('success to impliment')
        }
        

    })
});
