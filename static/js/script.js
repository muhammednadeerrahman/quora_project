$(document).on("submit", "form.ajax", function (e) {
    e.preventDefault()

   var $this  = $(this);

   document.onkeydown = function(evt){
    return false ;
    
   }
    var method =  $this.attr("method");
    var url =  $this.attr("action");
    var noLoader = $this.hasClass("no-loader");
    var noPopup = $this.hasClass("no-popup")
    var isRedirect = $this.hasClass("redirect");
    var isReload = $this.hasClass ("reload")

    if (!noLoader){
        Swal.showLoading()
    }
    $.ajax({
        method : method ,
        url : url,
        dataType : "json",
        data : new FormData (this),
        processData : false,
        contentType : false,
        Cache : false,
        success: function(data){
            if (!noLoader){
                Swal.hideLoading()
            }
            var message = data["message"];
            var title = data["title"];
            var status = data["status"];
            var redirect = data["redirect"]
            var redirect_url = data["redirect_url"]
            var stable = data["stable"];

            if (status === "success"){
                if (title){
                    title = title;
                }
                else{
                    title = 'success'
                }
                function doAfter(){
                    if (stable != "yes") {
                        if (isRedirect && redirect == "yes") {
                            window.location.href = redirect_url;
                        }
                        if (isReload) {
                            window.location.reload();
                        }
                    }
                }

                if (noPopup){
                    doAfter();
                }
                else{
                    Swal.fire({
                        icon: status,
                        title: title,
                        html: message,
                    }).then((result) =>{
                        console.log(result.isConfirmed)
                        if(result.isConfirmed){
                            doAfter();

                        }
                    })
                }
                document.onkeydown= function(evt){
                    return true ;

                };
            }
            else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }

                Swal.fire(title, message, "error");

                if (stable != "true") {
                    window.setTimeout(function () {}, 2000);
                }
                document.onkeydown = function (evt) {
                    return true;
                };
            }
        },

        error: function(data){

            Swal.hideLoading();
            var title = "An error occurred";
            var message = "An error occurred. Please try again later.";
            document.onkeydown = function (evt) {
                return true;
            };
            Swal.fire(title, message, "error");
        }
    })
});

$("a.action-button").on("click",function(e){
    e.preventDefault();
    console.log("helo")
    var $this = $(this);
    var text = $this.attr("data-text");
    var title = $this.attr("data-title");
    var confirmButtonText = "Yes";
    var confirmButtonColor = "#DD6B55";
    var type = "warning";
    var url = $this.attr("href");
    if (!title){
        title = "are you sure ?";
    }
    var isReload = $this.hasClass("reload");
    var isRedirect = $this.hasClass("redirect");
    var noResponsePopup = $this.hasClass("no-response-popup");
    swal.fire({
        icon : type,
        title: title,
        text: text,
        showCancelButton: true,
        confirmButtonText: confirmButtonText,
        confirmButtonColor: confirmButtonColor,
    }).then((result) =>{
        if (result.isConfirmed){
            Swal.showLoading();
            window.setTimeout(function(){
                $.ajax({
                    type : "get",
                    url : url,
                    dataType: "json",
                    success: function(data){
                        var message = data["message"]
                        var status = data["status"]
                        var redirect = data["redirect"]
                        var redirect_url = data["redirect_url"]
                        var stable = data["stable"]
                        var title = data["title"]

                        Swal.hideLoading();
                        if (status == "success") {
                            if (title) {
                                title = title;
                            } else {
                                title = "Success";
                            }

                            if (!noResponsePopup) {
                                Swal.fire({
                                    icon: "success",
                                    title: title,
                                    text: message,
                                    type: "success",
                                }).then((result) => {
                                    if (stable != "yes") {
                                        if (isRedirect && redirect == "yes") {
                                            window.location.href = redirect_url;
                                        }
                                        if (isReload) {
                                            window.location.reload();
                                        }
                                    }
                                });
                            }

                        }else {
                            if (title) {
                                title = title;
                            } else {
                                title = "An Error Occurred";
                            }

                            Swal.fire(title, message, "error");

                            if (stable != "true") {
                                window.setTimeout(function () {}, 2000);
                            }
                        }
                    },
                    error: function(data){
                        Swal.hideLoading();
                        var title = "An error occurred";
                        var message =
                            "An error occurred. Please try again later.";
                        Swal.fire(title, message, "error");
                    }
                })
            },100)
        }
    }) 
    });
