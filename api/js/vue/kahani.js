var baseComponent = Vue.extend({
  data: function() {
    return {
      loaded: [],
      current: 0,
      hasMore: "",
      nextItems: "",
      errors: []
    };
  },
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
  },
  methods: {
    fetchNext: function() {
      axios
        .get(this.nextItems)
        .then(response => {
          this.loaded = this.loaded.concat(response.data.content);
          this.hasMore = response.data.hasMore;
          this.nextItems = response.data.nextItem;
          this.current += 1;
        })
        .catch(e => {
          //TODO CLEAR errors before pushing
          this.errors.push(e);
        });
    },
    next: function() {
      if (this.current + 1 < this.loaded.length) {
        this.current += 1;
      } else if (this.hasMore == true) {
        this.fetchNext();
      }
    },
    prev: function() {
      this.current = this.current - 1 >= 0 ? this.current - 1 : 0;
    }
  },
  delimiters: ["[{", "}]"]
});

var kahaniComponent = baseComponent.extend({
  template: `
<div>
<ul v-if="errors && errors.length">
  <li v-for="error of errors">
    [{error.message}]
  </li>
</ul>

<div class="error-message" v-if="errors && errors.length">
  <div class="alert alert-danger alert-dismissible">
    <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
    <span v-for="error of errors">
      [{error.message}]
    </span>
  </div>
</div>

<div v-if="loaded && loaded.length" class="row justify-content-center">
  <div class="col-lg-8">
    <h3>
      <i class="fas fa-circle space-bottom-md color-pink"></i>
      <span>[{loaded[current].title}]</span>
    </h3>
    <h3 class="sub-heading2">[{loaded[current].author}]</h3>
    <center>
      <span v-on:click="prev">
        <i class="fas fa-chevron-circle-left color-change-hover color-pink"></i>
      </span>
      <span v-on:click="next">
        <i class="fas fa-chevron-circle-right color-change-hover color-pink"></i>
      </span>
    </center>
    [{loaded[current].kahaniText}]
  </div>
</div>
</div>`
});

new Vue({
  el: "#kahani",
  components: {
    "kahani-component": kahaniComponent
  }
});

/*
var content = baseComponent.extend({
  template: "#kahani"
});
*/
