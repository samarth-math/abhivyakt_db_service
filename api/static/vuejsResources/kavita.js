var poem = new Vue({
  el: '#kavita',
  data: {
    loadedPoems: [],
    currentRec: 0,
    hasMore:"",
    nextItems:"",
    errors: []
  },
  mounted() {
    axios.get("/kavitajs")
    .then(response => {
      this.loadedPoems = this.loadedPoems.concat(response.data.content)
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
        this.loadedPoems = this.loadedPoems.concat(response.data.content)
        this.hasMore = response.data.hasMore
        this.nextItems = response.data.nextItem
      }).catch(e => {
        //TODO CLEAR errors before pushing
        this.errors.push(e)
      })
    },
    nextPoem: function() {
      if (this.currentRec+1 < this.loadedPoems.length) {
        this.currentRec+=1
      } else {
        // TODO probably update currentRec in a promise
        this.fetchNext()
        this.currentRec+=1
      }
    },
    prevPoem: function() {
      this.currentRec = (this.currentRec-1>-1?this.currentRec-1:0)
    }
  },
  delimiters: ['[{', '}]']
})
