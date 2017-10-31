var home_module_handler = (function($) {
  var Module = {
    init: function(opts) {
      var self = this;
      self.opts = opts;

      $('input[type=file]').change(function(e){
        self.handle_file_browser_change(e);
      });
    },

    handle_file_browser_change: function(e) {
      var self = this,
          filename = e.target.files[0].name;

          console.log(filename);

      if (filename != undefined || filename != '') {
        $(e.currentTarget).next('.custom-file-control')
                          .attr('data-content', filename);
      }
    },

  };

  return Module;

})(jQuery);