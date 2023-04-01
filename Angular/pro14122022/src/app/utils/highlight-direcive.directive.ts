import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appHighlightDirecive]'
})
export class HighlightDirecive {
  @Input() appHighlightDirecive = '';
  constructor(private el:ElementRef) {    
   }
   @HostListener('mouseenter') onMouseEnter() {
    this.highlight( this.appHighlightDirecive || '');
  }  
  @HostListener('mouseleave') onMouseLeave() {
    this.highlight('');
  }  
  private highlight(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }

}
