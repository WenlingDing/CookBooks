/*global $ */
$(document).ready(function() {
  var counter = 1;
    $("#addrow").on("click", function() {
        var newRow = $("tr");
        var cols = " ";
        cols += '<td><textarea class="form-control" name="description"/></td>';
        cols += '<td class="col-sm-2"><a class="deleteRow"></a></td>';
        newRow.append(cols);
        
        $("table .order-list").append(newRow);
        counter ++;
    });
    
    $("table .order-list").on("click", ".deleteRow", function(event) {
        $(this).closest("tr").remove();
        counter -= 1;
    });
});