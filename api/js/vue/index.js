var featuredKavitaComponent = Vue.extend({
    mixins: [featuredObject],
    created() {
        this.fetchContent("/featured/kavita");
    }
});

var featuredKahaniComponent = Vue.extend({
    mixins: [featuredObject],
    created() {
        this.fetchContent("/featured/kahani");
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