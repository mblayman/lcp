import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('schools');
  this.route('login');
  this.route('signup');
  this.route('terms');
  this.route('contact');
  this.route('privacy');
  this.route('dashboard', function() {
    this.route('students', function() {
      this.route('new');
    });
    this.route('student', {path: '/students/:student_id'});
  });
});

export default Router;
