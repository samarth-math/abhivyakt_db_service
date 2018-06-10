var kahaniComponent = baseComponent.extend({
  created() {
    this.fetchContent("/kahanijs");
  }
});

new Vue({
  el: "#kahani",
  components: {
    "kahani-component": kahaniComponent
  },
  delimiters: ["[{", "}]"]
});
