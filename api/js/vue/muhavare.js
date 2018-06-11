var muhavareComponent = Vue.extend({
    mixins: [apiObject],
    created() {
        this.fetchContent("/muhavarejs");
    }
});

new Vue({
    el: "#muhavare",
    components: {
        "muhavare-component": muhavareComponent
    },
    delimiters: ["[{", "}]"]
});
