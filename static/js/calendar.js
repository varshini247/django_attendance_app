
//   console.log(document.getElementsByTagName("*"));
//   var col = (document.getElementsByTagName('span.date'))
//   console.log((col))
//   col.addEventListener('click', function onClick() {
//   col.style.backgroundColor = 'salmon';
//   col.style.color = 'white';
// });
function clickHandler() {
    // Here, `this` refers to the element the event was hooked on
    // console.log(id)
    if(typeof(abs)== 'undefined')
        {abs =[]}

    var status = $(this).attr("data-status")
    if(status == 0) {
      this.style.backgroundColor = "pink" 
      $(this).attr("data-status","1")
      abs.push(this.textContent)
      console.log(abs)
    }
    else{
      this.style.backgroundColor = "white"
      $(this).attr("data-status","0")
      abs.pop()
    }
    
    // $(this).toggleClass('active')
    console.log("ochindi")
    $('#save').click(function(){
  
      parameters =new URLSearchParams(window.location.search).get('month')
      console.log("paramsss"+ parameters)
  $.ajax({
      url: `/calendar?month=${parameters}`, // no domain needed. careful with CORS (search about it)
      type: 'GET',
      data: {"hehe": abs},
      traditional:true,
      success: function(response) {console.log(response.data)}, 
      // response will be what returned from python
      error: function (error){console.log(error)}
  })
  })
}
document.querySelectorAll('td').forEach(e => e.addEventListener("click", clickHandler))

$('#calculate').click(function(){
   console.log($('.marked--date').length)
   $('#dayform').toggle()
})

