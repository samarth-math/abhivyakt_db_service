var doheComponent = Vue.extend({
    mixins: [apiObject],
    created() {
        this.fetchContent("/dohejs");
    }
});

new Vue({
    el: "#dohe",
    components: {
        "dohe-component": doheComponent
    },
    delimiters: ["[{", "}]"]
});
