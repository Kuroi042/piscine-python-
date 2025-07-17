/**
 * @NApiVersion 2.x
 * @NScriptType UserEventScript
 */
define([], function() {
  function beforeLoad(context) {
    if (context.type === context.UserEventType.VIEW || context.type === context.UserEventType.EDIT) {
      var form = context.form;

      form.addButton({
        id: 'custpage_copy_3pl',
        label: 'Copy 3PL_QTY to Units',
        functionName: 'copy3PLToAdjustQty'
      });

      form.clientScriptModulePath = 'SuiteScripts/testme/test.js';
    }
  }

  return {
    beforeLoad: beforeLoad
  };
});
