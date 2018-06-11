var apiObject = {
    data: function() {
        return {
            loaded: [],
            current: 0,
            hasMore: "",
            nextItems: "",
            errors: []
        };
    },
    methods: {
        fetchContent: function(apiEndpoint) {
            axios
                .get(apiEndpoint)
                .then(response => {
                    this.loaded = this.loaded.concat(response.data.content);
                    this.hasMore = response.data.hasMore;
                    this.nextItems = response.data.nextItem;
                })
                .catch(e => {
                    this.errors.push(e);
                });
        },
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
    }
};
