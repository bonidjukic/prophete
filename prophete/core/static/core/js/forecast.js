var forecast_module_handler = (function($) {
  var Module = {
    init: function(opts) {
      var self = this;
      self.opts = opts;

      $('#calculate-forecast').on('click', function(e) {
        e.preventDefault();
        self.handle_submit(e);
      });
    },

    handle_submit: function(e) {
      var self = this,
          el = $(e.currentTarget);

      $.post({
        url: self.opts.submit_url,
        data : $("#config-form").serializeArray(),
        success: function(json) {
          if (json.success) {
            console.log('success');
          } else {
            console.log('error');
          }
        }
      });
    },
  };

  return Module;

})(jQuery);