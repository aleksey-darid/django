new Vue({
        el: '#schedule_app',
        data: {
            orders: []
        },
        created: function () {
            const vm = this;
            axios.get('/api/schedule')
                .then(function (response) {
                    console.log(response.data)
                })
        }
    }
)