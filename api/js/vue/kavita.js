var poem = new Vue({
  el: '#kavita',
  data: {
    loadedPoems: [],
    currentPoem: 0,
    hasMore:"",
    nextItems:"",
    errors: []
  },
  created() {
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
    fetchNextPoem: function() {
      axios.get(this.nextItems)
      .then(response => {
        this.loadedPoems = this.loadedPoems.concat(response.data.content)
        this.hasMore = response.data.hasMore
        this.nextItems = response.data.nextItem
        this.currentPoem+=1
      }).catch(e => {
        //TODO CLEAR errors before pushing
        this.errors.push(e)
      })
    },
    nextPoem: function() {
      if (this.currentPoem+1 < this.loadedPoems.length) {
        this.currentPoem+=1
      } else if (this.hasMore==true){
        this.fetchNextPoem()
      }
    },
    prevPoem: function() {
      this.currentPoem = (this.currentPoem-1>-1?this.currentPoem-1:0)
    }
  },
  delimiters: ['[{', '}]']
})
