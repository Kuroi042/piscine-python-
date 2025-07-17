/**
 * @NApiVersion 2.x
 * @NScriptType ClientScript
 */
define(['N/currentRecord'], function(currentRecord) {
  function copy3PLToAdjustQty() {
    var rec = currentRecord.get();

    var lineCount = rec.getLineCount({
      sublistId: 'inventory'
    });

    for (var i = 0; i < lineCount; i++) {
      var qty3PL = rec.getSublistValue({
        sublistId: 'inventory',
        fieldId: 'custcol_3pl_qty',
        line: i
      });

      if (qty3PL !== null && qty3PL !== '') {
        rec.setSublistValue({
          sublistId: 'inventory',
          fieldId: 'adjustqtyby',
          line: i,
          value: qty3PL
        });
      }
    }

    alert("3PL quantities copied to Adjust Qty. By!");
  }

  return {
    pageInit: function(context) {
      // Optional: Auto-run on page load
      // copy3PLToAdjustQty();
    },
    // If triggered by a button
    copy3PLToAdjustQty: copy3PLToAdjustQty
  };
});
