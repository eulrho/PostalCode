function auto_Complete() {
    let inputValue = $('#search-input').val();
    inputValue = String(inputValue);
    let address = {srchAddress:inputValue};   // test
    console.log(address)
    // ajax
    $.ajax({
      method: 'GET',
      url: 'http://localhost:5000/search',
      datatype: "json",
      // stringify : json 객체 -> string 객체
      data: address,
      contentType: "application/json",
      success: async function(result){
        console.log(result)
        let tag ="";
        // 자동완성 단어 리스트
        $.each(result, await function (key, value){
          let posList = value.postalcode, sidoList = value.sido, sigunguList = value.sigungu;
          let doroList = value.doro, bno1List = value.buildno1, bno2List = value.buildno2;
          let bnameList = value.buildname;
          console.log(posList, sidoList, sigunguList, doroList, bno1List, bno2List, bnameList)
          $(".searchList").empty();
          tag += '<li><p class="address">'+'('+posList+') '+sidoList+' '+sigunguList+' '+doroList+' '+bno1List+'-'+bno2List+' '+bnameList+'</p></li>';
        });
        console.time('append p tag')
        $(".searchList").append(tag);
        console.timeEnd('append p tag')
      },
      error: function (request, status, error){
        alert("ajax fail");
        alert(error);   // error 메세지
      }
    })}