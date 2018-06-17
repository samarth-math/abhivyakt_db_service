var featuredObject = {
    data: function() {
        return {
            loaded: [],
            current: 0,
            errors: []
        };
    },
    methods: {
        fetchContent: function(apiEndpoint) {
            axios
                .get(apiEndpoint)
                .then(response => {
                    this.loaded = response.data.content;
                })
                .catch(e => {
                    this.errors.push(e);
                });
        },
        next: function() {
            if (this.current + 1 < this.loaded.length) {
                this.current += 1;
            }
        },
        prev: function() {
            this.current = this.current - 1 >= 0 ? this.current - 1 : 0;
        }
    }
};
