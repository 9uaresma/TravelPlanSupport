const express = require('express');
const router = express.Router();

// Load cpp class
var Wrapper = require('bindings')('addon');
var planContainer = new Wrapper();

// variables
var place_num = 0;
var dep_month, dep_date, dep_hour, dep_min;

// Load home page
router.get('/', function(req, res, next){
  //User Agentの取得
  var userAgent = req.headers['user-agent'].toLowerCase();
  console.log("userAgent = ", userAgent);
  [dep_month, dep_date, dep_hour, dep_min] = planContainer.getDepartureDate();

  // 表示するページ出し分け
  if(userAgent.indexOf("android") != -1
    || userAgent.indexOf("iphone") != -1
    || userAgent.indexOf("ipod") != -1){
    callIndex(res, 'index_m');  // for smartPhone
  }
  else{
    callIndex(res, 'index');  // for PC
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
    // 出発日時をセットするボタンが押された時の処理
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
    // 予定追加ボタンを押した時の処理
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


function callIndex(res, index){
  // index: string index file to call
  res.render(index,{
    title: 'Travel Plan Support',
    places: planContainer.getPlans(),
    hours: planContainer.getHours(),
    ttl_hours: planContainer.getTtlHours(),
    place_num: place_num,
    dep_month: dep_month,
    dep_date: dep_date,
    dep_hour: dep_hour,
    dep_min: dep_min,
  });
}
