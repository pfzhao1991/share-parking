<template>
  <div>
      <mt-field id="extend" label="Remaining Time"></mt-field>
      <mt-field id="price" label="Price"></mt-field>
      <mt-cell id="pay" title="Payment" @click.native="choosePayment" :value="payment">
      </mt-cell>

      <mt-button id="confirm">Confirm</mt-button>

      <mt-picker v-show="selectPay" id="picker" :slots="slots" @change="changePayment"></mt-picker>
  </div>
  
</template>

<script>
import Vue from "vue";
import { Cell, Button, Picker, Field } from "mint-ui";

Vue.component(Cell.name, Cell);
Vue.component(Button.name, Button);
Vue.component(Picker.name, Picker);
Vue.component(Field.name, Field);

export default {
  name: "ExtendOrder",
  data() {
    return {
      selectPay: false,
      payment: 'Apple Pay',
      slots: [
        {
          flex: 1,
          values: ['Apple Pay','八达通','Ali Pay'],
          textAlign: 'center'
        }
      ]
    }
  },
  methods: {
    choosePayment: function() {
      this.selectPay = !this.selectPay;
    },
    changePayment(picker, values) {
      this.payment = values[0] || 'Apple Pay'
      this.selectPay = false
    }
  }
}
</script>

<style>

#confirm{
  background-color: #3e88fe;
  color: white;
  width: 80%;
  margin-top: 40px;
}

.mint-cell{
  text-align: left;
}

#picker {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.mint-field .mint-cell-title {
  width: 100%;
}

</style>