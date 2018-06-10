

var kahaniComponent = baseComponent.extend({});

new Vue({
  el: "#kahani",
  components: {
    "kahani-component": kahaniComponent
  },
  delimiters: ["[{", "}]"]
});

/*
var content = baseComponent.extend({
  template: "#kahani"
});
*/
