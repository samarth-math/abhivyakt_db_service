var kavitaComponent = Vue.extend({
    mixins: [apiObject],
    created() {
        this.fetchContent("/kavitajs");
    }
});

new Vue({
    el: "#kavita",
    components: {
        "kavita-component": kavitaComponent
    },
    delimiters: ["[{", "}]"]
});
