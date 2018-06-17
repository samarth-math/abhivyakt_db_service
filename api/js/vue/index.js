var featuredKavitaComponent = Vue.extend({
    mixins: [featuredObject],
    created() {
        this.fetchContent("/featuredkavitas");
    }
});

var featuredKahaniComponent = Vue.extend({
    mixins: [featuredObject],
    created() {
        this.fetchContent("/featuredkahanis");
    }
});

new Vue({
    el: "#index",
    components: {
        "featured-kavita-component": featuredKavitaComponent,
        "featured-kahani-component": featuredKahaniComponent
    },
    delimiters: ["[{", "}]"]
});