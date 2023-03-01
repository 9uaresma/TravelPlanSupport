const express = require('express');
const router = express.Router();


// cpp connection
var Wrapper = require('bindings')('addon');
var obj = new Wrapper();


let plans = [];
let hours = [];
var plan_num = 0;
let ttl_hours = 0

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {
     title: 'Travel Plan Support',
     plans: plans,
    //  hours: hours,
     plan_num,
     ttl_hours,
    });
});

router.post('/', function(req, res, next){
  const plan_name = req.body.plan;
  const plan_hour = req.body.hour;
  obj.setPlan(plan_name, Number(plan_hour));
  ttl_hours = obj.getTtlHours();
  console.log(obj.showPlan());

  plans.push([plan_name, plan_hour]);
  // hours.push(plan_hour);
  plan_num ++;
  res.redirect('/');
});

module.exports = router;
