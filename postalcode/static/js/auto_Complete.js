function auto_Complete() {
    let inputValue = $('#search-input').val();
    inputValue = String(inputValue);
    let postalcode = {input_pc:inputValue};   // test
    console.log(postalcode)
    // ajax
    $.ajax({
      method: 'GET',
      url: 'http://localhost:5000/ajax',
      datatype: "json",
      // stringify : json 객체 -> string 객체
      data: postalcode,
      contentType: "application/json",
      success: function(result){
        console.log(result)
        let tag ="";
        // 자동완성 단어 리스트
        $.each(result, function (key, value){
          let posList = value.postalcode
          console.log(posList)
          $(".searchList").empty();
          if(posList != ''){
            tag += '<li><svg class="submit-button"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#search"></use>\n' +
                    '</svg><p>' + posList + '</p></li>';
          }
        });
        $(".searchList").append(tag);
      },
      error: function (request, status, error){
        alert("ajax fail");
        alert(error);   // error 메세지
      }
    })
  }