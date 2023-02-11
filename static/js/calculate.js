function getPercentage(form) {
    // var form = document.forms['classform'];
    var percentage = form.elements['percent'].value;
    // console.log(percentage);
    return percentage;
}
function getTotalClasses(form) {
    // var form = document.forms['classform'];
    var totalClasses = form.elements['total_c'].value;
    // console.log(totalClasses);
    return totalClasses;
}
function getClassesAbsent(form) {
    // var form = document.forms['classform'];
    var classesAbsent = form.elements['absent_c'].value;
    return classesAbsent;
}
function calculate(formid) {
    var form = document.forms[formid];
    var total = parseInt(getTotalClasses(form));
    var absent = parseInt(getClassesAbsent(form));
    var reqPercent = parseInt(getPercentage(form));
    console.log(total, typeof (total), !(isNaN(total) == false));
    // console.log(reqPercent);
   
    if (isNaN(total) == false && isNaN(absent) == false && isNaN(reqPercent) == false) {
        var percent = computePercent(total-absent, total);
        var result = computeResult(total, absent, reqPercent);
        console.log("result is" + (result), isNaN(result),percent);
        if (isNaN(result)) {
            if (formid == "dayform"  ) {
                this.document.getElementsByClassName('result')[1].innerHTML = result + " "+ "more days!";
            }
            else {
                this.document.getElementsByClassName('result')[0].innerHTML = result+ " " + "more classes!";
            }
        
        }
        else if(typeof(result) == 'boolean'){
            if (formid == "dayform"  ) {
                this.document.getElementsByClassName('result')[1].innerHTML = "You have the required attendance!";
            }
            else {
                this.document.getElementsByClassName('result')[0].innerHTML = "You have the required attendance!";
            }
        }
        else {
            if (formid == 'classform') {
                this.document.getElementsByClassName('result')[0].innerHTML = "You can bunk" +" "+ result + " "+ "more classes :) ";
            }
            else {
                this.document.getElementsByClassName('result')[1].innerHTML = "You can bunk" + " "+ result + " "+"more days :) ";
            }

        }
        console.log( this.document.getElementsByClassName('percent'))
        this.document.getElementsByClassName('percent')[0].innerHTML = '<div class="percent-style">' + + percent + " %"+'</div>' 
    }

}
function computePercent(value, tvalue) {
    return Math.ceil((value / tvalue) * 100);
}
function computeResult(total, absent, reqPercent) {
 
    var result = null;
    var classesLeft = total - (reqPercent * total) / 100;
    if (absent < classesLeft) {
        result = Math.ceil(classesLeft - absent);
    }
    else if (absent == classesLeft) {
        result = true;
       
    }
    else {
        console.log("hi");
        result = "You need to attend " + Math.ceil((absent - classesLeft));
    }
    return result;
}