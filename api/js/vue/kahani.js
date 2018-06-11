var kahaniComponent = Vue.extend({
    mixins: [apiObject],
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
