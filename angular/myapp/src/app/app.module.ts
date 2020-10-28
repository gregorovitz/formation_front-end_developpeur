import { BrowserModule } from '@angular/platform-browser';
import { DEFAULT_CURRENCY_CODE, LOCALE_ID, NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { NavComponent } from './components/nav/nav.component';
import { RouterModule } from '@angular/router';
import { HomeComponent } from './features/home/home.component';
import { AboutComponent } from './features/about/about.component';
import { Demo1Component } from './features/demo1/demo1.component';
import { Demo2Component } from './features/demo2/demo2.component';
import { registerLocaleData } from '@angular/common';
import localeFR from '@angular/common/locales/fr';
import { Exo1Component } from './features/exo1/exo1.component';
import { TimePipe } from './time.pipe';

registerLocaleData(localeFR);
@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    NavComponent,
    HomeComponent,
    AboutComponent,
    Demo1Component,
    Demo2Component,
    Exo1Component,
    TimePipe
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot([
      {path: 'home', component:HomeComponent},
      {path: 'about', component:AboutComponent},
      {path: 'demo1', component:Demo1Component},
      {path: 'demo2', component:Demo2Component},
      {path: 'exo1',component:Exo1Component},
      //route2
    ])
  ],
  providers: [
    {provide:LOCALE_ID,useValue:'fr-Be'},
    {provide:DEFAULT_CURRENCY_CODE,useValue:'EUR'}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
