var dohe = new Vue({
    el: '#dohe',
    data: {
      loaded: [],
      current: 0,
      hasMore:"",
      nextItems:"",
      errors: []
    },
    mounted() {
      axios.get("/dohejs")
      .then(response => {
        this.loaded = this.loaded.concat(response.data.content)
        this.hasMore = response.data.hasMore
        this.nextItems = response.data.nextItem
      }).catch(e => {
        this.errors.push(e)
      })
    },
    methods: {
      fetchNext: function() {
        axios.get(this.nextItems)
        .then(response => {
          this.loaded = this.loaded.concat(response.data.content)
          this.hasMore = response.data.hasMore
          this.nextItems = response.data.nextItem
          this.current+=1
        }).catch(e => {
          //TODO CLEAR errors before pushing
          this.errors.push(e)
        })
      },
      next: function() {
        if (this.current+1 < this.loaded.length) {
          this.current+=1
        } else {
          this.fetchNext()
        }
      },
      prev: function() {
        this.current = (this.current-1 >= 0) ? this.current-1 : 0
      }
    },
    delimiters: ['[{', '}]']
  })
  