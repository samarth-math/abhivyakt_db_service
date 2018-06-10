var kahaniComponent = Vue.extend({
  mixins: [baseMixin],
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
