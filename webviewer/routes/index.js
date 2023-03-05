const express = require('express');
const router = express.Router();


// cpp connection
var Wrapper = require('bindings')('addon');
var planContainer = new Wrapper();

var plan_num = 0;

router.get('/', function(req, res, next){
  //User Agentの取得
  var userAgent = req.headers['user-agent'].toLowerCase();
  console.log("userAgent = ", userAgent);

  // 表示するページ出し分け
  if(userAgent.indexOf("android") != -1
    || userAgent.indexOf("iphone") != -1
    || userAgent.indexOf("ipod") != -1){
      res.render('index_m',{
        title: 'Travel Plan Support',
        plans: planContainer.getPlans(),
        hours: planContainer.getHours(),
        plan_num,
        ttl_hours: planContainer.getTtlHours(),
      });
  }
  else{
      res.render('index', {
        title: 'Travel Plan Support',
        plans: planContainer.getPlans(),
        hours: planContainer.getHours(),
        plan_num,
        ttl_hours: planContainer.getTtlHours(),
      });
  }
});

/**
 * POST: /
 */
router.post('/', (req, res, next) => {
  console.log("req.body = ", req.body);
  console.log("req.body.name = ", req.body.name);
  if(req.body.add){
    if(req.body.plan != 0 && req.body.hour != 0){
      console.log("submit");
      console.log(req.body);
      const plan_name = req.body.plan;
      const plan_hour = req.body.hour;
      planContainer.setPlan(plan_name, Number(plan_hour));

      plan_num ++;
      res.redirect('/');

    } else {
      console.log("input value !");
    }
  }
  else if(req.body.btn){
    const num = Number(req.body.num);
    console.log("num = ", req.body.num)
    console.log("num = ", num);
    
    if(req.body.num>0){
      console.log("swapPlan ↑");
      planContainer.swapPlanElements(num-1, num);
      res.redirect('/');
    }
    
  }else{
    console.log("else");
  }
  
});

module.exports = router;
