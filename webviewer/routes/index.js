const express = require('express');
const router = express.Router();


// cpp connection
var Wrapper = require('bindings')('addon');
var planContainer = new Wrapper();

var place_num = 0;

router.get('/', function(req, res, next){
  //User Agentの取得
  var userAgent = req.headers['user-agent'].toLowerCase();
  console.log("userAgent = ", userAgent);
  let dep_month = planContainer.getDepartureDate()[0];
  let dep_date = planContainer.getDepartureDate()[1];
  let dep_hour = planContainer.getDepartureDate()[2];
  let dep_min = planContainer.getDepartureDate()[3];

  // 表示するページ出し分け
  if(userAgent.indexOf("android") != -1
    || userAgent.indexOf("iphone") != -1
    || userAgent.indexOf("ipod") != -1){
      res.render('index_m',{
        title: 'Travel Plan Support',
        places: planContainer.getPlans(),
        hours: planContainer.getHours(),
        place_num: place_num,
        ttl_hours: planContainer.getTtlHours(),
        dep_month: dep_month,
        dep_date: dep_date,
        dep_hour: dep_hour,
        dep_min: dep_min,
      });
  }
  else{
      res.render('index', {
        title: 'Travel Plan Support',
        places: planContainer.getPlans(),
        hours: planContainer.getHours(),
        place_num: place_num,
        ttl_hours: planContainer.getTtlHours(),
        dep_month: dep_month,
        dep_date: dep_date,
        dep_hour: dep_hour,
        dep_min: dep_min,
      });
  }
});

/**
 * POST: /
 */
router.post('/', (req, res, next) => {
  console.log("req.body = ", req.body);
  if(req.body.add){
    if(req.body.place != 0 && req.body.hour != 0){
      console.log("submit");
      console.log(req.body);
      const place_name = req.body.place;
      const place_hour = req.body.hour;
      planContainer.setPlan(place_name, Number(place_hour));

      place_num ++;
      res.redirect('/');

    } else {
      console.log("input value !");
    }
  } else if(req.body.set_dep){
    let month = Number(req.body.dep_month);
    let date = Number(req.body.dep_date);
    let hour = Number(req.body.dep_hour);
    let min = Number(req.body.dep_min);
    if(month && date && hour && min){
      planContainer.setDepartureDate(month, date, hour, min);
      console.log("Departure Date & Time is set!");
      console.log("departure_date = ", planContainer.getDepartureDate());
      res.redirect('/');
    }

  } else if(req.body.btn){
    const num = Number(req.body.num);
    console.log("num = ", req.body.num)
    console.log("num = ", num);
    
    if(req.body.num>0){
      console.log("swapPlan ↑");
      planContainer.swapPlanElements(num-1, num);
      res.redirect('/');
    }
  } else {
    console.log("else");
  }
  
});

module.exports = router;
