source_count = 1;
data_variety_count = 1;

$('#btn-add-source').click( function() {
    source_count += 1;
    newRow = $("<div></div>").addClass("row");
    newCol = $("<div></div>").addClass("col-md-8");
    newFields = $("<div></div>").addClass("form-controls");
    newFields.append("<label>Source URL</label>");
    newFields.append($("<input>").attr({name:source_count+"_source_url"}).addClass("form-control"));
    newCol.append(newFields);
    newRow.append(newCol);

    newCol = $("<div></div>").addClass("col-md-4");
    newFields = $("<div></div>").addClass("form-controls");
    newFields.append("<label>Date Retrieved</label>");
    newFields.append($("<input>").attr({name:source_count+"_source_retrieved"}).addClass("form-control"));
    newCol.append(newFields);
    newRow.append(newCol);
    $("#source-material").append(newRow);
    $('#source_count').val(source_count);
});

$('#btn-add-data-variety').click( function() {
  data_variety_count += 1;
  newRow = $("<div></div>").addClass("row");
  newCol = $("<div></div>").addClass("col-md-8");
  newFields = $("<div></div>").addClass("form-group");
  newFields.append("<label>Variety</label>");

  dataVariety = $("<select></select>").attr({name:data_variety_count + "_data_variety", required:true}).addClass("form-control");
  dataVariety.append("<option value=\"\" selected disabled>-- Please Select --</option>");
  dataVariety.append("<option value=\"Credentials\">Authentication credentials</option>");
  dataVariety.append("<option value=\"Bank\">Bank account data</option>");
  dataVariety.append("<option value=\"Classified\">Classified information</option>");
  dataVariety.append("<option value=\"Copyrighted\">Copyrighted material</option>");
  dataVariety.append("<option value=\"Medical\">Medical records</option>");
  dataVariety.append("<option value=\"Payment\">Payment card data</option>");
  dataVariety.append("<option value=\"Personal\">Personal information</option>");
  dataVariety.append("<option value=\"Internal\">Sensitive organizational data</option>");
  dataVariety.append("<option value=\"System\">System information</option>");
  dataVariety.append("<option value=\"Secrets\">Trade secrets</option>");
  dataVariety.append("<option value=\"Unknown\">Unknown</option>");
  dataVariety.append("<option value=\"Other\">Other</option>");
  newFields.append(dataVariety);
  newCol.append(newFields);
  newRow.append(newCol);

  newCol = $("<div></div>").addClass("col-md-4");
  newFields = $("<div></div>").addClass("form-group");
  newFields.append("<label>Record count</label>");
  newFields.append($("<input>").attr({name:data_variety_count + "_data_count", required:true, type:"number"}).addClass("form-control"));
  newCol.append(newFields);
  newRow.append(newCol);
  $("#data-variety-array").append(newRow);
  $(data_variety_count+"_data_variety").focus();
});

$('#show_secondary_victim').click( function() {
  $('#secondary_victim_info').toggleClass("hidden");
  $('#second_vic').toggleClass("glyphicon-chevron-right").toggleClass("glyphicon-chevron-down");
  return false;
});

$('#show_victim_more_info').click( function() {
  $('#primary_victim_more_info').toggleClass("hidden");
  $('#vic_more').toggleClass("glyphicon-chevron-right").toggleClass("glyphicon-chevron-down");
  return false;
});