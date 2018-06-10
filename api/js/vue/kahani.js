var kahaniComponent = baseComponent.extend({
  created() {
    axios
      .get("/kahanijs")
      .then(response => {
        this.loaded = this.loaded.concat(response.data.content);
        this.hasMore = response.data.hasMore;
        this.nextItems = response.data.nextItem;
      })
      .catch(e => {
        this.errors.push(e);
      });
  }
});

new Vue({
  el: "#kahani",
  components: {
    "kahani-component": kahaniComponent
  },
  delimiters: ["[{", "}]"]
});
