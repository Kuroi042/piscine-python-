/**
 * @NApiVersion 2.x
 * @NScriptType ClientScript
 */
define(['N/currentRecord'], function(currentRecord) {
  function copy3PLToUnits() {
    var rec = currentRecord.get();
    var lineCount = rec.getLineCount({ sublistId: 'inventory' });

    for (var i = 0; i < lineCount; i++) {
      var qty3PL = rec.getSublistValue({
        sublistId: 'inventory',
        fieldId: 'custcol_3pl_qty', // replace with your actual 3PL_QTY field ID
        line: i
      });

      if (qty3PL !== null && qty3PL !== '') {
        rec.setSublistValue({
          sublistId: 'inventory',
          fieldId: 'adjustqtyby', // this is the units field on Inventory Adjustment
          line: i,
          value: qty3PL
        });
      }
    }

    alert('3PL quantities copied to Units!');
  }

  return {
    copy3PLToUnits: copy3PLToUnits
  };
});
